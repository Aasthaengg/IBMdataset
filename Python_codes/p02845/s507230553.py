n = int(input())
list1 = list(map(int,input().split()))

def count(n, list1):
    num0 = list1.count(0)
    statuslist = []
    answer = 1
    if num0 >= 4:
        return 0
    else:
        for i in range(len(list1)):
            if list1[i] == 0:
                    statuslist.append(0)
            else:
                pos = statuslist.count(list1[i]-1)
                answer *= pos
                try:
                    statuslist.remove(list1[i]-1)
                except ValueError:
                    return answer
                statuslist.append(list1[i])
        if num0 == 2 or num0 == 3:
            answer *= 6
        elif num0 == 1:
            answer *= 3  
        return (answer % 1000000007)
    # else:
    #     return 3
        

print(count(n, list1))