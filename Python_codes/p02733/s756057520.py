h,w,k = map(int,input().split())
cho=[input()for i in range(h)]

size=[[0]*h for i in range(1<<h)]
ans=[bin(x).count("1") for x in range(1<<h)]
for stage in range(w):
    new=[[0]*h for i in range(1<<h)]
    for column in range(h):
        if int(cho[column][stage]):
            for bit in range(1<<h):
                length=(((1<<column)-1) & bit).bit_length()
                new[bit][length]+=1
    for bit in range(1<<h):
        frag=True#Trueのままならnewを足し算
        for column in range(h):
            if new[bit][column]+size[bit][column]>k:
                if new[bit][column]>k:#一列の時点でkを超えていたらもう無理
                    ans[bit]+=1010
                frag=False
                ans[bit]+=1
                size[bit]=new[bit]
                break
        if frag:
            for column in range(h):
                size[bit][column]+=new[bit][column]
print(min(ans))