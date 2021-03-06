
import heapq
import sys
input = sys.stdin.readline

def main():
    num_sushi, chose_num = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(num_sushi)]

    data.sort(key=lambda x: -x[1])
    delicious_heap = []
    count_d, count_n = 0, 0
    neta_data = [0 for i in range(num_sushi + 1)]

    for i in range(chose_num):
        neta, oishisa = data[i]

        if neta_data[neta]:
            heapq.heappush(delicious_heap, oishisa)
        else:
            neta_data[neta] = 1
            count_n += 1

        count_d += oishisa

    ans = count_d + count_n ** 2

    for i in range(chose_num, num_sushi):
        if len(delicious_heap) == 0:
            break
        neta, oishisa = data[i]

        if neta_data[neta]:
            continue
        neta_data[neta] = 1
        count_n += 1
        pop_oishisa = heapq.heappop(delicious_heap)
        count_d += oishisa - pop_oishisa

        ans = max(ans, count_d + count_n ** 2)

    print(ans)


if __name__ == '__main__':
    main()