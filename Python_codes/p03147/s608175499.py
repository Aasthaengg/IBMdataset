N = int(input())
H = list(map(int,input().split()))

H_=H.copy()

def get_zero_idx(H_):
    zero_idx = []
    for i in range(len(H_)):
        if H_[i] == 0:
            zero_idx.append(i)
    return zero_idx

zero_idx = get_zero_idx(H_)
# print(zero_idx)
# print(H_)

ans=0

while True:
    zero_idx = get_zero_idx(H_)
#     print(zero_idx)
    #終了判定(全てのHが所定の高さを満たす)
    if len(zero_idx) == len(H_):
        break

    if len(zero_idx)==0:
        s=0
        e=N
        if s<e:
            for _ in range(s,e):
                H_[_]=H_[_]-1   
            ans +=1

    elif len(zero_idx)>=1:
        s=0
        e=zero_idx[0]
        if s<e:
            for _ in range(s,e):
                H_[_]=H_[_]-1   
            ans +=1
#         print('b',s,e,H_)

        for _ in range(1,len(zero_idx)):
            s=zero_idx[_-1]+1
            e=zero_idx[_]
            if s<e:
                for _ in range(s,e):
                    H_[_]=H_[_]-1   
                ans +=1
#             print('c',s,e,H_)

        s=zero_idx[-1]+1
        e=N
        if s < e:
            for _ in range(s,e):
                H_[_]=H_[_]-1   
            ans +=1
#         print('b-',s,e,H_)

print(ans)