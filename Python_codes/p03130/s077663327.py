import collections


def main():
    routeList = [list(map(int,input().split())) for _ in range(3)]
    routeList = [i for inner in routeList for i in inner]
    ansList = collections.Counter(routeList)
    
    for i in ansList:
        if ansList[i] == 3:
            print("NO")
            exit()
    print('YES')
    

    


if __name__== "__main__":
    main() 









