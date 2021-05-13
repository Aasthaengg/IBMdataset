A=list(input())
right_cnt=[0]
left_cnt=[0]
cnt=0
for i in range(len(A)):
   if A[i] == "<":
      right_cnt.append(right_cnt[-1]+1)
   else:
      right_cnt.append(0)
   if A[-i-1] == ">":
      left_cnt.append(left_cnt[-1]+1)
   else:
      left_cnt.append(0)
left_cnt=left_cnt[::-1]
for i in range(len(A)+1):
   cnt+=max(left_cnt[i],right_cnt[i])
print(cnt)