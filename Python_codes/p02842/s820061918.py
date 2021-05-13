N = int(input()) * 100
m = N // 108
if int(m * 1.08) == N//100:
    print(m)
elif int((m+1) * 1.08) == N//100:
    print(m+1)
else:
    print(":(")
