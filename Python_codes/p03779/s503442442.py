n = int(input())
if (int((2*n)**(1/2))+1)*(int((2*n)**(1/2)))/2 < n:
    print(int((2*n)**(1/2))+1)
else:
    print(int((2*n)**(1/2)))