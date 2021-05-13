n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:x[0], reverse=True)
print(lst[0][0] + lst[0][1])