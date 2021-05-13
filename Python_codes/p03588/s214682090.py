N = int(input())
li = [[int(i) for i in input().split()] for _ in range(N)]

li.sort(reverse=True)
print(sum(li[0]))
