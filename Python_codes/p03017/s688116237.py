def main():
    length, snuke_start, hnuke_start, snuke_goal, hnuke_goal = map(lambda x: int(x) - 1, input().split())
    grid = input()
    is_rock_continuing = False
    is_space_continuing = False
    if "##" in grid[min(snuke_start, hnuke_goal):max(snuke_goal, hnuke_goal) + 1]:
        is_rock_continuing = True
    if "..." in grid[hnuke_start - 1:hnuke_goal + 2]:
        is_space_continuing = True
    if snuke_goal < hnuke_goal and not is_rock_continuing:
        print("Yes")
    elif hnuke_goal < snuke_goal and not is_rock_continuing and is_space_continuing:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

