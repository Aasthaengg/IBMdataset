import sys

def main():
    lines = sys.stdin.readlines()

    # The number of rooms
    rooms = [0] * 10
    floors = [rooms] * 3
    buildings = [floors] * 4

    data_num = 0

    for index, line in enumerate(lines):
        #print(line)
        # rm '\n' from string of a line
        line = line.strip('\n')
        elems = line.split(" ")
        if index == 0:
            data_num = int(elems[0])
        else:
            b = int(elems[0]) - 1   # as index
            f = int(elems[1]) - 1   # as index
            r = int(elems[2]) - 1   # as index
            v = int(elems[3])       # as data
            # print v
            # print buildings[b][f][r]
            ans = []
            for b_i in range(0, 4):
                b_list = []
                for f_i in range(0, 3):
                    f_list = []
                    for r_i in range(0, 10):
                        if b == b_i and f == f_i and r == r_i:
                            f_list.append(buildings[b_i][f_i][r_i] + v)
                        else:
                            f_list.append(buildings[b_i][f_i][r_i])
                    b_list.append(f_list)
                ans.append(b_list)
            # print ans
            buildings = ans

    for b_i in range(0, 4):
        for f_i in range(0, 3):
            for r_i in range(0, 10):
                sys.stdout.write(' %d' % buildings[b_i][f_i][r_i])
            sys.stdout.write('\n')
        if b_i != 3:
            print "####################"



if __name__ == "__main__":
    main()