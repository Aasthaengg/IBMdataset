import sys

def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline

def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [k] = [int(input_raw[0])]
    input_raw = read_func().strip().split()
    num_list = []
    for i in range(k):
        num_list.append(long(input_raw[i]))

    max_num = long(2)
    min_num = long(2)
    is_exist = True
    if num_list[k-1] != 2:
        is_exist = False
    for i in range(k-1, -1, -1):
        if is_exist == False:
            break;
        min_min_num = min_num;
        #min_max_num = min_num + num_list[i] - 1
        #max_min_num = max_num;
        max_max_num = max_num + num_list[i] - 1
        if i > 0:
            min_min_num = num_list[i - 1] * (min_min_num / num_list[i - 1] + (0 if (min_min_num % num_list[i - 1] == 0)  else 1) )
            #min_max_num = num_list[i - 1] * long(min_max_num / num_list[i - 1] )
            #max_min_num = num_list[i - 1] * (max_min_num / num_list[i - 1] + (0 if (max_min_num % num_list[i - 1] == 0)  else 1) )
            max_max_num = num_list[i - 1] * long(max_max_num / num_list[i - 1] )

        min_num = min_min_num
        max_num = max_max_num

##        if(min_min_num > min_max_num and max_min_num > max_max_num):
##            is_exist = False
##            break;
##        elif(min_min_num > min_max_num and max_min_num <= max_max_num):
##            min_num = max_min_num
##            max_num = max_max_num
##        elif(min_min_num <= min_max_num and max_min_num > max_max_num):
##            min_num = min_min_num
##            max_num = min_max_num
##        else:
##            min_num = min(min_min_num, max_min_num)
##            max_num = max(min_max_num, max_max_num)
        if min_num > max_num:
            is_exist = False
            break;

    if is_exist == True:
        print min_num, max_num
    else:
        print -1


if __name__ == '__main__':
    main()
