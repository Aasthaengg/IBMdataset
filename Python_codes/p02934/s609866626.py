n = int(input())
a = list(map(int, input().split()))
deno = 0
for i in a:
    A = 1/i
    deno += A
print(1/deno)