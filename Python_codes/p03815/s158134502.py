x = int(input())
answer=(x // 11) * 2
if x % 11 >= 7:
    answer+=2
elif x % 11 ==0:
    pass
else:
    answer+=1
print(answer)