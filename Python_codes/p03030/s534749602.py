def main():
    n = int(input())
    inlis = []
    namelis = []
    for i in range(n):
        a, b = map(str, input().split())
        b = int(b)
        inlis.append([a,b])
        namelis.append(a)
    namelis.sort()    
    inlis_so = sorted(inlis)
    anslis = []
    for num in inlis:
        #print(num, num[0], inlis_so, inlis_so.count(num[0]))
        kazu = namelis.count(num[0])
        if kazu == 1:
            anslis.append(inlis_so.index(num)+1)
        else:
            kijun = namelis.index(num[0]) + 1
            kouho = list(filter(lambda word:True if word[0] == num[0] else False,inlis))
            kouho_so = sorted(kouho, key = lambda x:x[1], reverse = True)
            suujibun = kouho_so.index(num)
            anslis.append(kijun + suujibun)
    for i in range(1, n+1):
        #print(anslis)
        print(anslis.index(i)+1)

    

        
    
if __name__ == "__main__":
    main()
