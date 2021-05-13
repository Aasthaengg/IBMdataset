N = int(input())

odd_cnt = 0
ai = []
ai = input().split(" ")

for i in range(0,N,2):
    if (int(ai[i])%2) == 1:
        odd_cnt +=1

print(odd_cnt)