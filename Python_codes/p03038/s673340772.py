from heapq import heapify, heappop, heappush

def resolve():
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  sortedA = sorted(A)
  integraA = [0, sortedA[0]]

  # O[N]
  for i in range(1, N):
    integraA.append(integraA[-1] + sortedA[i])
  # print(integraA)
  # O[M]
  heap_tasks = []
  heapify(heap_tasks)
  for _ in range(M):
    B, C = map(int, input().split(" "))
    heappush(heap_tasks, ((-1)*C, B))
  

  # O[M]
  start_index = 0
  result = integraA[-1]
  for _ in range(M):
    task = heappop(heap_tasks)
    C = (-1) * task[0]
    B = task[1]
    # B が残りよりも多かった場合、残りに合わせる。
    if start_index + B > N:
      B = N - start_index

    if B == 0:
      break

    # print("task =", B, C)
    if sortedA[start_index + B - 1] <= C:
      # 対象範囲の全てが C より小さかったら全て置き換える。
      # print("diff", (integraA[start_index + B] - integraA[start_index]))
      result += B*C - (integraA[start_index + B] - integraA[start_index])
      start_index += B
      if start_index >= N:
        break
    elif sortedA[start_index] >= C:
      # 対象範囲の全てが C 以上だったら置き換えせずに終了。
      break
    else:
      # 対象範囲の一部が C 未満だったらその部分だけ置き換えて終了 (残りは全て C 以上になることが保証されているので)
      while sortedA[start_index + B - 1] > C:
        B -= 1
      result += B*C - (integraA[start_index + B] - integraA[start_index])
      break
  print(result)

if __name__ == "__main__":
  resolve()