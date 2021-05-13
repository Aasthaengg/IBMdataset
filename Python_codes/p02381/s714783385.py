while True:
    if input()=="0":
        break
    data = list(map(float,input().split()))
    ave = sum(data)/len(data)
    std_div = (sum([(ave-i)**2 for i in data]) /len(data))**(1/2)
    print(std_div)