def main():

    r,d,x = tuple([int(t)for t in input().split()])

    xs = [x]
    for i in range(10):
        xs.append(xs[i]*r-d)

    for a in xs[1:]:
        print(a)

if __name__ == "__main__":
    main()