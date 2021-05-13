#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))


s = input()

n = len(s)
s1 = s[0:(n-1)//2]
s2 = s[(n+3)//2-1:n+1]

if s == s[::-1]:
    if s1 == s1[::-1]:
        if s2 == s2[::-1]:
            print("Yes")
            exit()

print("No")
    

