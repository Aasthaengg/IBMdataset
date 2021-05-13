n,k=map(int,input().split())
h=list(map(int,input().split()))
print(sum([1 for i in h if i>=k]))
# 内包表記じゃなかったら
# count = 0
# for i in h_list:
#     if i >= K:
#         count += 1
# print(count)