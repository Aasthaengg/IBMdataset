import collections

np_list = input().split(" ")
N = int(np_list[0])
P = int(np_list[1])

sum = 0
S = list(map(lambda s:int(s),input()[::-1]))



if P == 2 or P == 5:
    for i in range(0,N):
        if S[i]%P == 0:
            sum += N-i
else :
    digit = 1
    rem_list = [0]
    for i in range(N):
        rem_list.append(((S[i]*digit)%P+rem_list[i])%P)
        digit *= 10
        digit %= P
    c = collections.Counter(rem_list[1:])
    for i in range(1,N+1):
        if rem_list[i] == 0:
            sum += 1
        temp =c[rem_list[i]]
        temp -=1
        sum += temp
        c[rem_list[i]] = temp
print(sum)
