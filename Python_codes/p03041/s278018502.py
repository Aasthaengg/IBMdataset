n,k=map(int, input().split())
s=input()

s_list=list(s)

s_list[k-1]=s_list[k-1].lower()

print("".join(s_list))