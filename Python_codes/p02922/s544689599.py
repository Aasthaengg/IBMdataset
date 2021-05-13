A, B = map(int, input().split())
cnt =  0
outlet = 1

while outlet < B:
    outlet -= 1
    outlet += A
    cnt += 1
print(cnt)
