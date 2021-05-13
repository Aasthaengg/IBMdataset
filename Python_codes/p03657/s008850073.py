A,B = map(int,input().split())
ans_list = [A%3,B%3,(A+B)%3]
print('Possible') if 0 in ans_list else print('Impossible')