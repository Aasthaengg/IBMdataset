mark_list=[1,2,3,'∞']
n=int(input())
element_x=[int(i) for i in input().split()]
element_y=[int(l) for l in input().split()]
for p in mark_list:
    if p==1:
        m_distance=0
        for o in range(n):
            x=element_x[o]
            y=element_y[o]
            m_distance+=abs(x-y)
        print(m_distance)
    if p==2:
        y_distance=0
        y_distance2=0
        for m in range(n):
            x=element_x[m]
            y=element_y[m]
            y_distance2+=pow(abs(x-y),2)
        y_distance=pow(y_distance2,0.5)
        print(y_distance)
    if p==3:
        third_distance=0
        third_distance2=0
        for q in range(n):
            x=element_x[q]
            y=element_y[q]
            third_distance2+=pow(abs(x-y),3)
        third_distance=pow(third_distance2,1/3)
        print(third_distance)
    if p=='∞':
        c_distance=0
        difference=0
        for r in range(n):
            x=element_x[r]
            y=element_y[r]
            difference=abs(x-y)
            if difference>c_distance:
                c_distance=difference
        print(c_distance)
