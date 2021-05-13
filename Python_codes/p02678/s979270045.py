from collections import deque
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    distances = [-1] * N
    instructions = [-1] * N
    distances[0] = 0
    d = deque([0])
    while d:
        current_room = d.popleft()
        for next_room in graph[current_room]:
            if distances[next_room] == -1 or distances[current_room] + 1 < distances[next_room]:
                distances[next_room] = distances[current_room] + 1
                instructions[next_room] = current_room
                d.append(next_room)
    print('Yes')
    for v in instructions[1:]:
        print(v+1)


if __name__ == '__main__':
    main()
