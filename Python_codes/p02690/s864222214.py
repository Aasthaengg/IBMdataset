
def main():
    x = int(input())
    kouhodic = dict()
    for i in range(200):
        kouhodic[i ** 5] = i
        kouhodic[-i ** 5] = -i
    
    kouhodic = sorted(kouhodic.items())
    kazu = len(kouhodic)
    #print(kouhodic)

    for i in range(kazu):
        for j in range(i+1, kazu):
            if kouhodic[j][0] - kouhodic[i][0] == x:
                print(kouhodic[j][1], kouhodic[i][1])
                exit()
    
    
    




if __name__ == "__main__":
    main()