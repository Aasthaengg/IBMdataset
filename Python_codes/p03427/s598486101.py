N = input()

cnt = sum(list(map(int, N)))
kyuu = (int(len(N))-1) * 9 + int(N[0]) -1
if cnt > kyuu:
    print(cnt)
else:
    print(kyuu)




