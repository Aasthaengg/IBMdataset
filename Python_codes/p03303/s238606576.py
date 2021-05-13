s=input()
n = int(input())

ans=[s[i] for i in range(len(s)) if i%n==0]

print(''.join(ans))