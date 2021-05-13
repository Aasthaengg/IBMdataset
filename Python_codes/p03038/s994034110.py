N, M = map(int, input().split())
As = list(map(int, input().split()))
BCs = [list(map(int, input().split())) for _ in range(M)]

BCs = sorted(BCs,reverse = True, key = lambda x: x[1])
As = sorted(As, key = lambda x:x)

#%%
A_ind = 0

for BC in BCs:
    count = BC[0]
    value = BC[1]
    
    for i in range(count):
        if As[A_ind] < value:
            As[A_ind] = value
            A_ind += 1
            if A_ind >= len(As):
                break
        else:
            break
        
    else:
        continue
    break

print(sum(As))