ab=input().split()
a=int(ab[0])
b=int(ab[1])
ans_list=[a+b,a-b,a*b]
ans_list.sort()
ans=ans_list[2]
print(ans)