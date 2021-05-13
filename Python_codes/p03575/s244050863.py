def main():
    n, m = map(int, input().split())
    array = [[] for _ in range(n+1)]
    temp = []
    for _ in range(m):
        a, b = map(int, input().split())
        array[a].append(b)
        array[b].append(a)
        temp.append([a, b])
    result = 0
    from collections import deque
    while len(temp) > 0:
        a, b = temp.pop()
        array[a].remove(b)
        array[b].remove(a)
        d = deque([1])
        pop = d.pop
        append = d.append
        flag = [True] * (n + 1)
        while len(d) > 0:
            now = pop()
            for to in array[now]:
                if flag[to]:
                    append(to)
                    flag[to] = False
        for f in flag[1:]:
            if f:
                result += 1
                break
        array[a].append(b)
        array[b].append(a)
    print(result)
main()