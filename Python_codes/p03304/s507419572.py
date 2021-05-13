N = input().split()

n = float(N[0])
m = float(N[1])
d = float(N[2])

#max_point = m-1
#total = n**m
#total_point = 0.
#point_sub = 0
#point_m = m-d
#point_m_sub = m
#for i in range(point_m):
#    point_sub += point_m_sub*(n-i)
#    point_m_sub -= 1

#print(str(point_sub/total))
if d == 0:
    ans = (m-1)/n
    print(str(ans))
else:
    ans = 2*(m-1)*(n-d)/n**2
    print(str(ans))


#for i in range(int(max_point)):
#    total_point += (n-d-i)*(m-i)

#print(str(total_point/total))