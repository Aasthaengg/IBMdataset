s = input()
n = int(input())

for i in range(n):
    p = input().split()

    a, b = [int(x) for x in p[1:3]]
    if p[0]=="print":
        print(s[a:b+1])
    elif p[0]=="replace":
        s = s[:a] + p[3] + s[b+1:]
    elif p[0]=="reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]