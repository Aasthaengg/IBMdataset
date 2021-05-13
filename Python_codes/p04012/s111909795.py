def main():
    w = list(input())
    oklist=[]
    for i in range(len(w)):
        w1 = w.count(w[i])
        if w1 % 2 != 0:
            oklist.append(1)
    if oklist == []:
        print('Yes')
    else:
        print('No')
    
    
if __name__ == '__main__':
  main()