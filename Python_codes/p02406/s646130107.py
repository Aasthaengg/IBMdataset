n = int(input())
# i = 0
# 
# while i < n:
#     i = i + 1
#     if i % 3 == 0 or i % 10 == 3:
#         print(' ' + str(i),end='')
# 
# print()

s=""
for i in range(1,n+1):
    if i%3==0:
        s+=" "+str(i)
    elif "3" in list(str(i)):
        s+=" "+str(i)
print(s)