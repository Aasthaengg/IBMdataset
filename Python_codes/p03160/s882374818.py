N=int(input())
height_list=list(map(int,input().split()))
score_list=[ 0, abs(height_list[0]-height_list[1]) ]



for i in range(2,N):

    tmp=min(
        abs(height_list[i]-height_list[i-1])+score_list[i-1],
        abs(height_list[i]-height_list[i-2])+score_list[i-2]
    )

    score_list.append(tmp)

print(score_list[N-1])

