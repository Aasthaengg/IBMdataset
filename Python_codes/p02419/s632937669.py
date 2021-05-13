W = input()
cnt = 0
while True:
    T = input()
    if T == "END_OF_TEXT":
        break
    
    T = list(T.lower().split())
    for S in T:
        if S == W:
            cnt += 1
print(cnt)