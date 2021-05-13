n, m = map(int, input().split())
mod = lambda x:x%n+1
for i in range((m+1)//2):
    print(mod(-i-(m+1)//2), mod(i+1-(m+1)//2))
for i in range(m//2):
    print(mod(-i+m//2), mod(i+2+m//2))