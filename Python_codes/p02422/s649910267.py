x = input()
N = int(input())
p = [input().split() for _ in range(N)]
for i in p:
    a,b= int(i[1]), int(i[2]) + 1
    if i[0] == 'replace':
        x = x[:a]+ i[3] + x[b:]
    elif i[0] =='reverse':
        x = x[:a] + x[a:b][::-1] + x[b:]
    elif i[0] == 'print':
        print(x[a:b])

