N,A,B = map(int, input().split())

if (B-A)%2 == 0:
    #真ん中で会う
    ans = (B-A)//2
else:
    if N-B < A-1:
        #まずBがNへ行く
        temp_ans = N-B
        A += N-B
        ans = temp_ans + 1 + (N-A)//2
    else:
        #まずAが1へ行く
        temp_ans = A-1
        B -= A-1
        ans = temp_ans + 1 + (B-1)//2
print(ans)