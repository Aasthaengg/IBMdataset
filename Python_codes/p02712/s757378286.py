n = int(input())
sum_n = (1/2)*n*(n+1)
sum_3 = (1/2)*(n//3)*(n//3+1)*3
sum_5 = (1/2)*(n//5)*(n//5+1)*5
sum_15 = (1/2)*(n//15)*(n//15+1)*15
print(str(int(sum_n+sum_15-sum_3-sum_5)))