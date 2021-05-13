import itertools
def main():
  N = int(input())
  posi = []
  for i in range(N):
    posi.append(list(map(int, input().split())))
  posi.sort()
  num = [i for i in range(N)]
  ans = 1000000000
  for pair in itertools.combinations(num,2):
    p = posi[pair[1]][0]-posi[pair[0]][0]
    q = posi[pair[1]][1]-posi[pair[0]][1]
    ch = [True]*N
    ans_temp = 0
    for i in range(N):
      if ch[i]:
        ans_temp += 1
        ch[i] = False
      now = posi[i]
      while [now[0] +  p, now[1] + q] in posi:
        ch[posi.index([now[0] +  p, now[1] + q])] = False
        now = [now[0] +  p, now[1] + q]
    ans = min(ans, ans_temp)
  if N == 1:
    ans = 1
  print(ans)
    
  
if __name__ == "__main__":
  main()