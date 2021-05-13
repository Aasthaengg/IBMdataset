# coding=utf-8


def main():
    def sub():
        n = input()
        i = 1
        s = ''
        # ---------------------------------------------------------------------
        # CHECK_NUM
        while True:
            x = i
            if x % 3 == 0:
                s += ' '+str(i)
                # -----------------------
                # END_CHECK_NUM
                i += 1
                if i <= n:
                    # goto CHECK_NUM
                    continue
                else:
                    # END!!
                    break
                # -----------------------
            # -----------------------------------------------------
            # INCLUDE3
            while True:
                if x % 10 == 3:
                    s += ' '+str(i)
                    # -----------------------
                    # END_CHECK_NUM
                    i += 1
                    if i <= n:
                        # goto INCLUDE3
                        break
                    else:
                        # END!!
                        return s
                    # -----------------------
                else:
                    x /= 10
                    if x:
                        # goto INCLUDE3
                        continue
                    else:
                        # -----------------------
                        # END_CHECK_NUM
                        i += 1
                        if i <= n:
                            # goto CHECK_NUM
                            break
                        else:
                            # END!!
                            return s
                        # -----------------------
            # -----------------------------------------------------
        # ---------------------------------------------------------------------
        return s
    print sub()

if __name__ == '__main__':
    main()