#https://atcoder.jp/contests/abc165/tasks/abc165_b
N= int(input(" "))

M= 100
i= 0

while 1:
    M= M + M//100
    i = i+1
    if M >= N:
        print(i)
        break