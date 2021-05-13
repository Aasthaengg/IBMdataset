S = input()
N = len(S)

r_S = S[::-1]

head_S = S[0: int((N - 1) / 2)]
r_head_S = head_S[::-1]

end_S = S[int((N+3)/2 - 1) : N+1]
r_end_S = end_S[::-1]

if S == r_S and head_S == r_head_S and end_S == r_end_S:
    print("Yes")
else:
    print("No")
