#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

n = int(input())
s = input()

x = [0]

for i in range(n):
    if (s[i] == "I"):
        x.append(x[i] + 1)
    else:
        x.append(x[i] - 1)
#print(x)
print(max(x))
