if __name__ == '__main__':
    s=input()
    count=0
    for i in s:
        if i=="o":
            count+=1
    if 15- len(s) >=8-count:
        print("YES")
    else:
        print("NO")