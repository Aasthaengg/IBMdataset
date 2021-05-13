#-*-coding:utf-8-*-

def main():
    s = input()

    string_list=list(str(s))

    if string_list[0]==string_list[1]==string_list[2]:
        print("Yes")
    elif string_list[1]==string_list[2]==string_list[3]:
        print("Yes")
    else:
        print("No")
    
if __name__=="__main__":
    main()