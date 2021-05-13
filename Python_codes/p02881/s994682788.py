#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

def divisors(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            if (i*i != n):
                table.append(n//i)
        i+=1
    return table

n = int(input())

tbl = divisors(n)
ans = []

for i in tbl:
    tmp = i + n//i -2
    ans.append(tmp)

print(min(ans))

