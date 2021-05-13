MALE = 0
FEMALE = 1

def query(i):
    print(i, flush=True)
    s = input()
    if s == 'Vacant':
        exit()

    if s == 'Male':
        return(MALE)
    else:
        return(FEMALE)

def search(start, end, start_gendar):
    i = (end - start)//2
    g = query(start + i)
    if (i%2 == 0 and g != start_gendar) or (i%2 != 0 and g == start_gendar):
        return (start, start+i, start_gendar)
    return (start+i, end, g)

def main():
    n = int(input())
    start = 0
    end = n
    gendar = query(0)
    for i in range(20):
        start_new, end_new, gendar_new = search(start, end, gendar)
        start = start_new
        end = end_new
        gendar = gendar_new

if __name__ == "__main__":
    main()