N = int(input())
a_s = list(map(int,input().split()))
answer = 0
for a in a_s:
    NUM = a
    while NUM % 2 == 0:
        NUM//=2
        answer += 1
print(answer)